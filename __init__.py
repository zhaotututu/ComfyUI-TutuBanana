from .Tutu import NODE_CLASS_MAPPINGS as TUTU_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS as TUTU_DISPLAY_MAPPINGS, WEB_DIRECTORY
from .TutuPromptMasterV3 import NODE_CLASS_MAPPINGS as PROMPT_V3_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS as PROMPT_V3_DISPLAY_MAPPINGS
from .TutuNanoBananaPro import NODE_CLASS_MAPPINGS as BANANA_PRO_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS as BANANA_PRO_DISPLAY_MAPPINGS
import aiohttp.web
from .template_adapter import PromptTemplateAdapter
from .user_templates_manager import UserTemplatesManager
import server
import os
import json
from pathlib import Path

# 合并所有节点映射
NODE_CLASS_MAPPINGS = {**TUTU_MAPPINGS, **PROMPT_V3_MAPPINGS, **BANANA_PRO_MAPPINGS}
NODE_DISPLAY_NAME_MAPPINGS = {**TUTU_DISPLAY_MAPPINGS, **PROMPT_V3_DISPLAY_MAPPINGS, **BANANA_PRO_DISPLAY_MAPPINGS}

# --- Tutu API ---
# Initialize adapter once
ADAPTER_INSTANCE = PromptTemplateAdapter()
USER_TEMPLATES_MANAGER = UserTemplatesManager()

# Base directory for this extension
EXTENSION_DIR = Path(__file__).parent

@server.PromptServer.instance.routes.get("/tutu/categories")
async def get_tutu_categories(request: aiohttp.web.Request):
    """
    API endpoint to get all template categories.
    Query params:
    - lang: 'zh' or 'en' (default: 'zh')
    """
    try:
        lang = request.query.get("lang", "zh")
        categories = ADAPTER_INSTANCE.get_all_categories(lang)
        return aiohttp.web.json_response(categories)
    except Exception as e:
        import traceback
        print(f"Error in /tutu/categories: {e}")
        traceback.print_exc()
        return aiohttp.web.json_response({"error": str(e)}, status=500)


@server.PromptServer.instance.routes.get("/tutu/templates")
async def get_tutu_templates(request: aiohttp.web.Request):
    """
    API endpoint to get templates by category.
    ?category=<category_id>
    """
    category_id = request.query.get("category", None)
    
    if not category_id:
        return aiohttp.web.json_response(
            {"error": "Category ID is required"}, status=400
        )
    
    try:
        # The frontend doesn't need language-specific templates from this endpoint,
        # it gets both and switches locally.
        templates = ADAPTER_INSTANCE.get_templates_by_category(category_id)
        return aiohttp.web.json_response(templates)
    except Exception as e:
        # Adding traceback for better debugging
        import traceback
        print(f"Error in /tutu/templates: {e}")
        traceback.print_exc()
        return aiohttp.web.json_response(
            {"error": str(e)}, status=500
        )


@server.PromptServer.instance.routes.get("/tutu/images/{image_path:.*}")
async def get_tutu_image(request: aiohttp.web.Request):
    """
    Serve image files from the gpt4o-image-prompts-master directory
    Example: /tutu/images/333.jpeg
    """
    try:
        image_path = request.match_info['image_path']
        
        # Construct full path to image
        full_path = EXTENSION_DIR / "gpt4o-image-prompts-master" / "gpt4o-image-prompts-master" / "images" / image_path
        
        # Security check: ensure the path is within our images directory
        if not full_path.is_relative_to(EXTENSION_DIR):
            return aiohttp.web.Response(status=403, text="Forbidden")
        
        # Check if file exists
        if not full_path.exists() or not full_path.is_file():
            return aiohttp.web.Response(status=404, text="Image not found")
        
        # Determine content type based on file extension
        ext = full_path.suffix.lower()
        content_types = {
            '.jpeg': 'image/jpeg',
            '.jpg': 'image/jpeg',
            '.png': 'image/png',
            '.gif': 'image/gif',
            '.webp': 'image/webp'
        }
        content_type = content_types.get(ext, 'application/octet-stream')
        
        # Read and return the file
        with open(full_path, 'rb') as f:
            return aiohttp.web.Response(
                body=f.read(),
                content_type=content_type
            )
    
    except Exception as e:
        import traceback
        print(f"Error serving image: {e}")
        traceback.print_exc()
        return aiohttp.web.Response(status=500, text="Internal server error")


# ===== User Templates API =====

@server.PromptServer.instance.routes.get("/tutu/user-templates")
async def get_user_templates(request: aiohttp.web.Request):
    """Get all user-created templates"""
    try:
        templates = USER_TEMPLATES_MANAGER.get_all_templates()
        return aiohttp.web.json_response(templates)
    except Exception as e:
        import traceback
        print(f"Error in /tutu/user-templates: {e}")
        traceback.print_exc()
        return aiohttp.web.json_response({"error": str(e)}, status=500)


@server.PromptServer.instance.routes.post("/tutu/user-templates")
async def create_user_template(request: aiohttp.web.Request):
    """Create a new user template"""
    try:
        data = await request.json()
        result = USER_TEMPLATES_MANAGER.create_template(data)
        
        if result.get("success"):
            return aiohttp.web.json_response(result, status=201)
        else:
            return aiohttp.web.json_response(result, status=400)
    
    except Exception as e:
        import traceback
        print(f"Error creating user template: {e}")
        traceback.print_exc()
        return aiohttp.web.json_response({"error": str(e)}, status=500)


@server.PromptServer.instance.routes.put("/tutu/user-templates/{template_id}")
async def update_user_template(request: aiohttp.web.Request):
    """Update a user template"""
    try:
        template_id = request.match_info['template_id']
        data = await request.json()
        result = USER_TEMPLATES_MANAGER.update_template(template_id, data)
        
        if result.get("success"):
            return aiohttp.web.json_response(result)
        else:
            return aiohttp.web.json_response(result, status=404 if "not found" in result.get("error", "") else 400)
    
    except Exception as e:
        import traceback
        print(f"Error updating user template: {e}")
        traceback.print_exc()
        return aiohttp.web.json_response({"error": str(e)}, status=500)


@server.PromptServer.instance.routes.delete("/tutu/user-templates/{template_id}")
async def delete_user_template(request: aiohttp.web.Request):
    """Delete a user template"""
    try:
        template_id = request.match_info['template_id']
        result = USER_TEMPLATES_MANAGER.delete_template(template_id)
        
        if result.get("success"):
            return aiohttp.web.json_response(result)
        else:
            return aiohttp.web.json_response(result, status=404 if "not found" in result.get("error", "") else 400)
    
    except Exception as e:
        import traceback
        print(f"Error deleting user template: {e}")
        traceback.print_exc()
        return aiohttp.web.json_response({"error": str(e)}, status=500)

# AI nodes only - removed AiHelper and UI components
__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS', 'WEB_DIRECTORY']

